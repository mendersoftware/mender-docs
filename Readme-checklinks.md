# checklinks

`checklinks` is a `node.js` script based upon the
[`remark-validate-links`](https://github.com/remarkjs/remark-validate-links)
tool. It validates all internal links (i.e., [foobar](#install)).

The tool if run automatically collects the mark

# Install

The tool has a few `node.js` requirements. If you already have `node` installed on your system, run:

```bash 
$ npm install
```

in the documentation directory.

# Usage

To run the command:

```bash
$ checklinks
```
This will run the checker on all the documentation files in the repository,
and fail if any files, or sections if a link is not found.

## Note

A few things to keep in mind:

* The checker does not verify sections in the `200.APIs/*` folder, as these
  files are automatically generated from [`swagger`](https://swagger.io/), and
  not present when the tool is run.
* The header slug is a modified Github header slugger, which collapses multiple dashes into one. That is slug(---) -> slug(-). This is because Grav, which our documentation uses does not fully support the Github slug format.
