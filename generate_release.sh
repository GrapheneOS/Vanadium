#!/bin/bash

set -o errexit

KEYSTORE=$PWD/vanadium.keystore
APKSIGNER=$PWD/third_party/android_sdk/public/build-tools/29.0.2/apksigner
BUNDLETOOL=$PWD/build/android/gyp/bundletool.py

read -p "Enter keystore passphrase: " -s keystore_pass
echo

cd out/Default/apks

rm -rf release
mkdir release
cd release

$BUNDLETOOL build-apks --bundle ../TrichromeChrome.aab --output TrichromeChrome.apks --mode=universal --ks $KEYSTORE --ks-pass file:/dev/stdin --ks-key-alias vanadium <<< $keystore_pass
unzip TrichromeChrome.apks universal.apk
mv universal.apk TrichromeChrome.apk

for app in TrichromeLibrary TrichromeWebView; do
    $APKSIGNER sign --ks $KEYSTORE --ks-pass file:/dev/stdin --ks-key-alias vanadium --in ../$app.apk --out $app.apk <<< $keystore_pass
done
