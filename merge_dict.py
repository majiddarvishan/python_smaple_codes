#Merge dictionaries with sub dictionaries
def deep_dict_merge(dct1, dct2, override=True):
  """
  :param dct1: First dict to merge
  :param dct2: Second dict to merge
  :param override: if same key exists in both dictionaries, should override? otherwise ignore. (default=True)
  :return: The merge dictionary
  """
  
  import copy
  import collections

  merged = copy.deepcopy(dct1)
  for k, v2 in dct2.items():
    if k in merged:
      v1 = merged[k]
      if isinstance(v1, dict) and isinstance(v2, collections.Mapping):
        merged[k] = deep_dict_merge(v1, v2, override)
      elif isinstance(v1, list) and isinstance(v2, list):
        merged[k] = v1 + v2
      else:
        if override:
          merged[k] = copy.deepcopy(v2)
    else:
      merged[k] = copy.deepcopy(v2)
  return merged


d1 = {"v1": "value1", "sub": {"sv1": "sub value 1",'newsub':"value 2",'newsubdict':{'ok':'pssible','not_again':{'key1':'just checking'}}}}
d2 = {"v2": "value2", "sub": {"sv2": "sub value 2",'newsubdict':{'fine':'i am working','not_again':{'key2':'Am i right?'}}}}

d3 = deep_dict_merge(d1, d2)
print(d3)
