# Humana Language Prototype

Humana is an experimental programming language that aims to read like plain
English. It keeps syntax minimal and focuses on clarity. This directory contains
a very small prototype showing how such a language could work.

## Files

- `grammar.ebnf` – outline of the language grammar.
- `examples.hmn` – small snippets demonstrating the syntax.
- `transpiler.py` – sketch of a transpiler from Humana to JavaScript.
- `runtime.js` – starter runtime helpers for tasks and logging.

## Multithreading Design Plan

`start a task` should spawn real threads in the browser. There are two possible
strategies:

1. **Web Workers** – The transpiler can wrap a block of Humana code in a worker
   script. `start a task to` would generate code that creates a `Worker` with the
   block body. Shared data can be passed via `postMessage` and
   `onmessage` handlers. `wait for` would await a message from that worker.

2. **WASM threads** – When compiled to WebAssembly with threads enabled, each
   `start a task` becomes a new thread using WebAssembly's `spawn` primitives.
   Shared memory would be implemented with `SharedArrayBuffer`. This approach is
   more complex but gives higher performance.

The runtime (`runtime.js`) provides helper functions `startTask` and `waitFor`
that encapsulate worker creation and message handling. The transpiler can import
these helpers so users only write high level instructions.
