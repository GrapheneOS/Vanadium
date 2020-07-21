#!/bin/bash

set -o errexit -o nounset -o pipefail

KEYSTORE=$PWD/../vanadium.keystore
APKSIGNER=$PWD/third_party/android_sdk/public/build-tools/29.0.2/apksigner

read -p "Enter keystore passphrase: " -s keystore_pass
echo

cd out/Default/apks

rm -rf release
mkdir release
cd release

for app in TrichromeChrome TrichromeLibrary TrichromeWebView; do
    $APKSIGNER sign --ks $KEYSTORE --ks-pass file:/dev/stdin --ks-key-alias vanadium --in ../${app}6432.apk --out $app.apk <<< $keystore_pass
done
