### S1 | type: add | dimension: vocabulary-member | symbol: path_tools_py3tool_py
- Needs: n8 (t2:s2)
- Searches tried: "tools/py3tool.py", "py3tool.py", "file path", widen "tools/py3tool.py file path" → path_ipython_core_magics_basic_py, path_numpy_core_fromnumeric_py, path_gcloud_pubsub_subscription_py, path_sklearn_linear_model_logistic_py (all code paths for different modules); no entry for tools/py3tool.py exists.
- Meaning: Source code file path to the Python 3 conversion tool script: tools/py3tool.py.
- Category: code-value
- Contextual aliases: tools/py3tool.py, tools_py3tool_py
- Example: `TERM code_entity(file=path_tools_py3tool_py, kind="script", name="py3tool.py") -> code_entity_2 : TERM`
- Contrast: not a general module path or package name
- Proposed record: `{"symbol": "path_tools_py3tool_py", "kind": "value", "category": "code-value", "definition": "Source code file path to the Python 3 conversion tool script: tools/py3tool.py.", "not": "a general module path or package name", "aliases": ["tools/py3tool.py", "tools_py3tool_py"]}`
