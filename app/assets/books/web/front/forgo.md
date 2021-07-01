# forgo
Tiny UI runtime

https://forgojs.org/

```js
import { rerender } from "forgo";

function SimpleTimer(initialProps) {
  let seconds = 0; // Just a regular variable, no hooks!

  return {
    render(props, args) {
      setTimeout(() => {
        seconds++;
        rerender(args.element); // rerender
      }, 1000);

      return (
        <div>
          {seconds} seconds have elapsed... {props.firstName}!
        </div>
      );
    },
  };
}
```