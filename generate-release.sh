#!/bin/bash

[[ $# -ge 1 ]] || exit 1

set -o errexit -o nounset -o pipefail

KEYSTORE=$PWD/../vanadium.keystore
APKSIGNER=$PWD/third_party/android_sdk/public/build-tools/34.0.0/apksigner
readonly APPS=(
    TrichromeChrome
    TrichromeLibrary
    TrichromeWebView
)

read -p "Enter keystore passphrase: " -s keystore_pass
echo

for d in "$@"; do
    cd "$d/Default/apks"

    rm -rf release
    mkdir release
    cd release

    for app in ${APPS[@]}; do
        $APKSIGNER sign --ks $KEYSTORE --ks-pass file:/dev/stdin --ks-key-alias vanadium --in ../${app}*.apk --out $app.apk <<< $keystore_pass
    done

    cd ../../../..
done
