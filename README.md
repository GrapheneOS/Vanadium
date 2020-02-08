Vanadium is a privacy and security hardened variant of Chromium providing the WebView (used by
other apps to render web content) and standard browser for [GrapheneOS](https://grapheneos.org).
It depends on hardening and compatibility fixes in GrapheneOS rather than reinventing the wheel
inside Vanadium. For example, GrapheneOS already provides a hardened malloc implementation so
there's no need for Vanadium to replace it. Similarly, it can deploy security features causing
breakage on other operating systems due to the ability to fix compatibility problems in the OS.

See [the official build documentation](https://grapheneos.org/build#browser-and-webview) for build
instructions.
