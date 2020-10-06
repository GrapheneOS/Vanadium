#!/bin/bash

set -o errexit -o nounset -o pipefail

KEYSTORE=$PWD/../vanadium.keystore
APKSIGNER=$PWD/third_party/android_sdk/public/build-tools/30.0.1/apksigner
BUNDLETOOL=$PWD/build/android/gyp/bundletool.py
AAPT2=$PWD/third_party/android_build_tools/aapt2/aapt2

read -p "Enter keystore passphrase: " -s keystore_pass
echo

cd out/Default/apks

rm -rf release
mkdir release
cd release

$BUNDLETOOL build-apks --aapt2 $AAPT2 --bundle ../TrichromeChrome6432.aab --output TrichromeChrome.apks --mode=universal --ks $KEYSTORE --ks-pass file:/dev/stdin --ks-key-alias vanadium <<< $keystore_pass
unzip TrichromeChrome.apks universal.apk
mv universal.apk TrichromeChrome.apk

for app in TrichromeLibrary TrichromeWebView; do
    $APKSIGNER sign --ks $KEYSTORE --ks-pass file:/dev/stdin --ks-key-alias vanadium --in ../${app}6432.apk --out $app.apk <<< $keystore_pass
done
