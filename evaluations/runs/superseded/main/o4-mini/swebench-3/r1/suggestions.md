### S1 | type: add | dimension: vocabulary-member | symbol: create_file
- Needs: n14 (t1:s15)
- Searches tried: `node /kit/rag.mjs search "Create file test.py" --kind action` → no create or touch operation
- signature: ACTION create_file(path: STRING) -> REF[STRING]
- meaning: Create a new empty file at the given path and return its reference identity.
- not: modify_code (which applies structured edits to existing files)
- aliases: touch, make_file
- Proposed record:
  {"symbol":"create_file","kind":"operation","signature":"(path: STRING) -> REF[STRING]","definition":"Create a new file at the specified path and return a runtime reference.","not":"modify_code","aliases":["touch","make_file"]}

### S2 | type: add | dimension: vocabulary-member | symbol: install_package
- Needs: n17 (t1:s19)
- Searches tried: `node /kit/rag.mjs search "install pytest" --kind action` → no installation operation
- signature: ACTION install_package(package: ATOM[platform_label], version: STRING) -> void
- meaning: Install the specified package at the given version into the runtime environment.
- not: run_tests (which executes tests, not package installs)
- aliases: pip_install, pkg_install
- Proposed record:
  {"symbol":"install_package","kind":"operation","signature":"(package: ATOM[platform_label], version: STRING) -> void","definition":"Install the named software package at the specified version.","not":"run_tests","aliases":["pip_install","pkg_install"]}