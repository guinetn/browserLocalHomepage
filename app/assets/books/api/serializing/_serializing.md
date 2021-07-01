# Serializing

# Serialization 
object → restorable data format
process of turning some object into a data format that can be restored later. People often serialize objects in order to save them to storage, or to send as part of communications.

# Deserialization 
object  ← restorable data format
reverse of that process, taking data structured from some format, and rebuilding it into an object. 
Popular data format for serializing data is JSON. Before that, it was XML.

Many  languages offer a native capability for serializing objects. These native formats usually offer more features than JSON or XML, including customizability of the serialization process.

Unfortunately, the features of these native deserialization mechanisms can be repurposed for malicious effect when operating on untrusted data. Attacks against deserializers have been found to allow denial-of-service, access control, and remote code execution (RCE) attacks.


download.page(api/serializing/json.md)
::::
download.page(api/serializing/jsonp.md)
::::
download.page(api/serializing/yaml.md)
::::
download.page(api/serializing/raml.md)
::::
in python: see `import pickle` 
