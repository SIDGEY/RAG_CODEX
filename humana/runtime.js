// Simple runtime helpers for Humana
// The real implementation would handle workers and message passing.

export function startTask(fn) {
  const workerBlob = new Blob([`onmessage = () => {(${fn})();}`], { type: 'application/javascript' });
  const worker = new Worker(URL.createObjectURL(workerBlob));
  return worker;
}

export function waitFor(worker) {
  return new Promise(resolve => {
    worker.onmessage = () => resolve();
  });
}

export function say(msg) {
  console.log(msg);
}
