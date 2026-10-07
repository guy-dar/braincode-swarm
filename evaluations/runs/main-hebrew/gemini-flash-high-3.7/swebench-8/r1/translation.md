<|user|>בינאריים מקובץ cross אינם בשימוש עבור ConfigTool (ש-LLVM תלוי בו)
זה בבנייה של mesa. בעת הרצה עם קובץ cross שמכיל



```

[binaries]

llvm-config = ''

```



זה עדיין מוצא את ה-llvm-config של מכונת הבנייה שלי וממשיך כאילו הכל היה בסדר:



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



הטלאי הבא גורם לדברים לעבוד, אך לא בטוח אם זו הגישה הנכונה:



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



נראה שכל זה צריך להיות מרוכז קצת, אך לא בטוח ב-100% איפה.
<|assistant|>1. שנה את mesonbuild/dependencies/base.py
