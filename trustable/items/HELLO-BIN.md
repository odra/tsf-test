---
normative: true
# Used to specify a Validator and its arguments.
evidence: 
  type: "hello_bin"
  configuration:
    src: src/hello.c
    dest: _build/hello
references:
  - type: "file"
    path: "_build/hello" 
score:
  lrossett: 1.0
  odra: 0.8
---

Hello builds as expected
