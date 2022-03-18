#!/bin/bash

[[ $# -eq 1 ]] || exit 1

set -o errexit -o nounset -o pipefail

KEYSTORE=$PWD/../vanadium.keystore
APKSIGNER=$PWD/third_party/android_sdk/public/build-tools/31.0.0/apksigner

read -p "Enter keystore passphrase: " -s keystore_pass
echo

cd "$1/Default/apks"

rm -rf release
mkdir release
cd release

for app in TrichromeChrome TrichromeLibrary TrichromeWebView; do
    $APKSIGNER sign --ks $KEYSTORE --ks-pass file:/dev/stdin --ks-key-alias vanadium --in ../${app}6432.apk --out $app.apk <<< $keystore_pass
done
