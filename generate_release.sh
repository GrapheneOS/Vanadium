#!/bin/bash

ANDROID_TOP=~/android/grapheneos
KEYSTORE=$PWD/vanadium.keystore
APKSIGNER=$PWD/third_party/android_sdk/public/build-tools/29.0.2/apksigner

cd out/Default/apks

rm -f TrichromeChrome.apks
rm -f TrichromeChrome.apk

java -jar $ANDROID_TOP/prebuilts/bundletool/bundletool-all-20190905.jar build-apks --bundle TrichromeChrome.aab --output TrichromeChrome.apks --mode=universal --ks $KEYSTORE --ks-pass pass:vanadiumpass --ks-key-alias vanadiumkey
unzip TrichromeChrome.apks universal.apk
mv universal.apk TrichromeChrome.apk

for app in TrichromeLibrary TrichromeWebView; do
    $APKSIGNER sign --ks $KEYSTORE --ks-pass pass:vanadiumpass --ks-key-alias vanadiumkey $app.apk
done
