solutions = [
  {
    'name': 'src',
    'url': 'https://chromium.googlesource.com/chromium/src.git',
    'managed': False,
    'custom_deps': {
    },
    'custom_vars': {
      'checkout_pgo_profiles': True,
    },
  },
]
hooks = [
  {
    'name': 'fetch_filter_lists',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist.txt',
              '--urls',
              'https://easylist-downloads.adblockplus.org/antiadblockfilters.txt',
              'https://easylist.to/easylist/easylist.txt',
              'https://easylist.to/easylist/easyprivacy.txt']
  },
  {
    'name': 'fetch_filter_lists_arabic',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_arabic.txt',
              '--urls',
              'https://easylist-downloads.adblockplus.org/liste_ar.txt']
  },
  {
    'name': 'fetch_filter_lists_bulgaria',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_bulgaria.txt',
              '--urls',
              'http://stanev.org/abp/adblock_bg.txt']
  },
  {
    'name': 'fetch_filter_lists_spanish',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_spanish.txt',
              '--urls',
              'https://easylist-downloads.adblockplus.org/easylistspanish.txt']
  },
  {
    'name': 'fetch_filter_lists_french',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_french.txt',
              '--urls',
              'https://easylist-downloads.adblockplus.org/liste_fr.txt']
  },
  {
    'name': 'fetch_filter_lists_germany',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_germany.txt',
              '--urls',
              'https://easylist.to/easylistgermany/easylistgermany.txt']
  },
  {
    'name': 'fetch_filter_lists_hebrew',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_hebrew.txt',
              '--urls',
              'https://raw.githubusercontent.com/easylist/EasyListHebrew/master/EasyListHebrew.txt']
  },
  {
    'name': 'fetch_filter_lists_indian',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_indian.txt',
              '--urls',
              'https://easylist-downloads.adblockplus.org/indianlist.txt']
  },
  {
    'name': 'fetch_filter_lists_indonesia',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_indonesia.txt',
              '--urls',
              'https://raw.githubusercontent.com/heradhis/indonesianadblockrules/master/subscriptions/abpindo.txt']
  },
  {
    'name': 'fetch_filter_lists_italy',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_italy.txt',
              '--urls',
              'https://easylist-downloads.adblockplus.org/easylistitaly.txt']
  },
  {
    'name': 'fetch_filter_lists_korean',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_korean.txt',
              '--urls',
              'https://easylist-downloads.adblockplus.org/koreanlist.txt']
  },
  {
    'name': 'fetch_filter_lists_lithuanian',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_lithuanian.txt',
              '--urls',
              'https://raw.githubusercontent.com/EasyList-Lithuania/easylist_lithuania/master/easylistlithuania.txt']
  },
  {
    'name': 'fetch_filter_lists_latvian',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_latvian.txt',
              '--urls',
              'https://raw.githubusercontent.com/Latvian-List/adblock-latvian/master/lists/latvian-list.txt']
  },
  {
    'name': 'fetch_filter_lists_dutch',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_dutch.txt',
              '--urls',
              'https://easylist-downloads.adblockplus.org/easylistdutch.txt']
  },
  {
    'name': 'fetch_filter_lists_nordic',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_nordic.txt',
              '--urls',
              'https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/NordicFiltersABP-Inclusion.txt']
  },
  {
    'name': 'fetch_filter_lists_polish',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_polish.txt',
              '--urls',
              'https://easylist-downloads.adblockplus.org/easylistpolish.txt']
  },
  {
    'name': 'fetch_filter_lists_portuguese',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_portuguese.txt',
              '--urls',
              'https://easylist-downloads.adblockplus.org/easylistportuguese.txt']
  },
  {
    'name': 'fetch_filter_lists_romanian',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_romanian.txt',
              '--urls',
              'https://zoso.ro/pages/rolist.txt']
  },
  {
    'name': 'fetch_filter_lists_russian',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_russian.txt',
              '--urls',
              'https://easylist-downloads.adblockplus.org/ruadlist.txt']
  },
  {
    'name': 'fetch_filter_lists_vietnam',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_vietnam.txt',
              '--urls',
              'https://abpvn.com/filter/abpvn-IPl6HE.txt']
  },
  {
    'name': 'fetch_filter_lists_china',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/filter_lists/filter_list_download.py',
              '--output',
              'src/vanadium/android_config/filter_lists/filter_lists_easylist_china.txt',
              '--urls',
              'https://easylist-downloads.adblockplus.org/easylistchina.txt']
  },
  {
    'name': 'apply_subprojects_patches',
    'condition': 'checkout_android',
    'action': ['python3',
              'tools/common/apply_subprojects_patches.py',
              '--base_patch_dir',
              'subprojects_patches',
              '--src_dir',
              'src']
  },
]
target_os = ['android']
