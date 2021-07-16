# solidjs

https://www.solidjs.com/

efficient and flexible JavaScript library for building user interfaces.

reactive state-based micro-library 
similar API to React and Preact
as fast as vanilla JS in render performance

```js
import { render } from "solid-js/web";
import { onCleanup, createSignal } from "solid-js";

const CountingComponent = () => {
  const [count, setCount] = createSignal(0);
  const interval = setInterval(
    () => setCount(count => count + 1),
    1000
  );
  onCleanup(() => clearInterval(interval));
  return <div>Count value is {count()}</div>;
};

render(() => <CountingComponent />, document.getElementById("app"));
```