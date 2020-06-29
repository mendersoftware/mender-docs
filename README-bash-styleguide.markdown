# Bash style guide

This is a short guide on how the Bash (CLI) examples in this documenation is to
be structured.

## Code blocks

### Highlighting

#### CLI commands

Code blocks with shell commands should always have the `bash` tag, for syntax highlighting.

i.e.

```````
 ```bash
 echo foobar
 ```
```````

Not

``````
```console
echo foobar
```
``````

#### Scripts

Scripts should always have the `bash` tag, for syntax highlighting. That is:

```````
```bash
#! /bin/bash
echo foobar
```
```````

### Remove the prompt string

__PS__, or the _prompt string_ should always be removed from the CLI examples.
This makes copy-pasting the examples straight forward. That is:

```````
```bash
echo foobar
```
```````

Not

```````
```bash
$ echo foobar
```
```````

### Code output

Output from code examples should follow all the rules above, except that the
prompt string is encouraged. The syntax highlighting should be `bash`.
Output should also be formatted in a quote block. That is:

```````
> ```bash
> $ echo foobar
> foobar
> ```
```````

Not

```````
```bash
echo foobar
foobar
```
```````


## Variables

Variables should always use the `${VARIABLE}` syntax. That is:

```````
```bash
cd "${VAR}"
```
```````

Not

```````
```bash
cd $VAR
```
```````

## Long lines

If commands grow too long, wrap them over multiple lines through escaping the line. That is:

```````
```bash
SOME_ENV_VAR=foobar bash-script --flag1 arg1 \
                                --flag2 arg2 \
                                ...
```
```````

Not

```````
```bash
SOME_ENV_VAR=foobar bash-script --flag1 arg1 --flag2 arg2 ...
```
```````
