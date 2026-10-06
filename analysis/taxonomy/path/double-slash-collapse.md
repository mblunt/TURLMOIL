# Double Slash Collapse

**Description:** Some parsers collapse consecutive `//` or multiple slashes in the path while others preserve them, especially for file:// and other special schemes.

| Pair | URL | path_a | path_b |
|------|-----|--------|--------|
| javascript-whatwg vs javascript-deno | `file://///DSZj0MUIs2ATk65Ylw5O@.2-:2020yrimsl6B^M54409438L#` | `///DSZj0MUIs2%0BATk65Ylw5O@.2-:2020yrimsl6B%5EM54409438L` | `/DSZj0MUIs2%0BATk65Ylw5O@.2-:2020yrimsl6B^M54409438L` |
| javascript-whatwg vs javascript-deno | `file://////fE5A@1e9ar9S:831j1G4sju8W2GJ0m028g?#` | `////fE5A@1e9ar9S:831j1G4sju8W2GJ0m028g` | `/fE5A@1e9ar9S:831j1G4sju8W2GJ0m028g` |
| rust-url vs elixir-uri | `file://///DSZj0MUIs2ATk65Ylw5O@.2-:2020yrimsl6B^M54409438L#` | `/DSZj0MUIs2%0BATk65Ylw5O@.2-:2020yrimsl6B^M54409438L` | `///DSZj0MUIs2ATk65Ylw5O@.2-:2020yrimsl6B^M54409438L` |
| go-net vs rust-url | `data:////7RM9xc8@Y32Bz57.8Q-Cj3hbz2C:6788,4B304v3A4J?#` | `//7RM9xc8@Y32Bz57.8Q-Cj3hbz2C:6788,4B304v3A4J` | `//7RM9%F1%86%AE%BEc8@Y32Bz57.8Q-Cj3hbz2C:6788,4B304v3A4J` |
| go-net vs rust-url | `data://////3T1S54Lxyz@[a:A:5:c0:C:d:ad:b]:59887lp8B971G0:17o468?#` | `////3T1S54Lxyz@[a:A:5:c0:C:d:ad:b]:59887lp8B971G0:17o468` | `////3T1S54L%F3%95%97%92&%F3%B1%A2%BAbcr8T2Y7@[a:A:5:c0:C:d:ad:b]:59887lp8B971G0:17o468` |
| cpp-ada-url vs rust-url | `file://////fE5abc@1e9ar9S:831j1G4sju8W2GJ0m028g?#` | `/fE5abc@1e9ar9S:831j1G4sju8W2GJ0m028g` | `////fE5abc@1e9ar9S:831j1G4sju8W2GJ0m028g` |
| cpp-ada-url vs rust-url | `file:////7Sxyz@84:744jJox27qm8;3l3U4I7v?#` | `/7Sxyz@84:744jJox27qm8;3l3U4I7v` | `//7Sxyz@84:744jJox27qm8;3l3U4I7v` |
