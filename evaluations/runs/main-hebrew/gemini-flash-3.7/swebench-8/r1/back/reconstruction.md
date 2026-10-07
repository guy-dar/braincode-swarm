<|user|>Cross-file binaries not used for ConfigTool (which LLVM depends on)
This is in a mesa build. When running with a cross file containing

```
[binaries]
llvm-config = ''
```

it still finds my build machine's llvm-config and continues as if everything was fine:

```
The Meson build system
Version: 0.45.0.dev1
Source dir: /home/ilia/src/mesa-meson
Build dir: /home/ilia/src/mesa-meson/armv7-build
Build type: cross build
Program python found: YES (/usr/bin/python)
Project name: mesa
Native C compiler: cc (gcc 6.4.0 "gcc (Gentoo 6.4.0 p1.1) 6.4.0")
Cross C compiler: /usr/bin/armv7a-hardfloat-linux-gnueabi-gcc (gcc 4.9.4)
Native C++ compiler: c++ (gcc 6.4.0 "c++ (Gentoo 6.4.0 p1.1) 6.4.0")
Cross C++ compiler: /usr/bin/armv7a-hardfloat-linux-gnueabi-g++ (gcc 4.9.4)
...
Found llvm-config: /usr/lib/llvm/4/bin/llvm-config (4.0.1)
Dependency LLVM found: YES
```

The following patch gets things working, but not sure this is the right approach:

```
diff --git a/mesonbuild/dependencies/base.py b/mesonbuild/dependencies/base.py
index e29d4de5..66f6b015 100644
--- a/mesonbuild/dependencies/base.py
+++ b/mesonbuild/dependencies/base.py
@@ -211,7 +211,21 @@ class ConfigToolDependency(ExternalDependency):
     def __init__(self, name, environment, language, kwargs):
         super().__init__('config-tool', environment, language, kwargs)
         self.name = name
-        self.tools = listify(kwargs.get('tools', self.tools))
+
+        if self.want_cross:
+            self.tools = []
+            if self.tool_name not in environment.cross_info.config['binaries']:
+                if self.required:
+                    raise DependencyException('%s binary missing from cross file' % self.tool_name)
+            else:
+                tool = environment.cross_info.config['binaries'][self.tool_name]
+                potential_toolbin = ExternalProgram(tool, silent=True)
+                if potential_toolbin.found():
+                    self.tools = [potential_toolbin.get_command()[0]]
+                else:
+                    mlog.debug('Cross %s not found.' % potential_toolbin.name)
+        else:
+            self.tools = listify(kwargs.get('tools', self.tools))
 
         req_version = kwargs.get('version', None)
         tool, version = self.find_config(req_version)
```

Seems like this all needs to be centralized a bit, but not 100% sure where.
<|assistant|>1. Modify mesonbuild/dependencies/base.py
