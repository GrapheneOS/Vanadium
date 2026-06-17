#!/usr/bin/env python3

import argparse
import os
import pathlib
import subprocess
import sys


subprojects_dir_to_patches_dir = {
  'v8': 'v8',
  'third_party/search_engines_data/resources': 'third_party/search_engines_data/resources',
}


def ApplySubprojectPatches(args):
    src_dir = args.src_dir
    base_patch_dir = args.base_patch_dir
    for subproject_dir_rel_src in subprojects_dir_to_patches_dir:
        subproject_patches_rel_src = subprojects_dir_to_patches_dir[subproject_dir_rel_src]
        subproject_dir = os.path.join(src_dir, subproject_dir_rel_src)
        if os.path.exists(os.path.join(subproject_dir, '.git/rebase-apply')):
            am_abort_cmd = ['git', '-C', str(subproject_dir), 'am', '--abort']
            print(f'aborting previous patch application for {subproject_dir_rel_src}')
            subprocess.run(am_abort_cmd).check_returncode()
        # Rough check for now when patches are applied manually or automatically in subproject
        diff_check_cmd = ['git', '-C', str(src_dir), 'diff', '--', str(subproject_dir_rel_src)]
        diff_check_output = subprocess.check_output(diff_check_cmd)
        if diff_check_output.decode() != "":
            print('Skipping patch application to subproject directory: '
                  + str(subproject_dir_rel_src) + ', already applied patches via hooks')
            continue
        patches_dir_path = pathlib.Path(os.path.join(base_patch_dir, subproject_patches_rel_src))
        patches_paths = sorted(patches_dir_path.glob('*.patch'))
        for patches_path in patches_paths:
            patches_path_abs = os.path.abspath(patches_path)
            git_am_cmd = ['git', '-C', str(subproject_dir),
                          'am', '--whitespace=nowarn', '--keep-non-patch', patches_path_abs]
            git_am_completed_proc = subprocess.run(git_am_cmd, capture_output=True)
            git_am_stdout_str = git_am_completed_proc.stdout.decode('utf-8')
            git_am_stdout_lines = git_am_stdout_str.splitlines()
            git_am_patch_msg = git_am_stdout_lines[0].replace('Applying: ', '')
            if git_am_completed_proc.returncode != 0:
                if git_am_patch_msg.startswith('[tmp]') or git_am_patch_msg.startswith('[upstream]'):
                    print(f'Skipping: {git_am_patch_msg}')
                    git_am_skip_cmd = ['git', '-C', str(subproject_dir),
                                       'am', '--skip']
                    subprocess.run(git_am_skip_cmd).check_returncode()
                    continue
                print(f'Aborting, failed to apply: {git_am_patch_msg}')
                git_am_abort_cmd = ['git', '-C', str(subproject_dir),
                                    'am', '--abort']
                subprocess.run(git_am_abort_cmd).check_returncode()
                git_am_completed_proc.check_returncode()
            else:
                print(f'Applied: {git_am_patch_msg} successfully')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src_dir', required=True,
                        help='Relative directory for chromium src dir')
    parser.add_argument('--base_patch_dir', required=True,
                        help='Base directory where subproject patches are found')
    ApplySubprojectPatches(parser.parse_args(sys.argv[1:]))
