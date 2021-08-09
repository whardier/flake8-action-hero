# flake8-action-hero
A plugin for flake8 that performs conditional FIXME/TODO checks.

## Action Tags

Code comments that begin with `# FIXME:`/`# TODO:` are often referred to as "FIXME Comments".  This plugin refers to them as action tags.

Action tags are typically a tag followed by a series of commands and variables.  The series is defined by the module (action) handling the conditional test defined in sections below.

The parser for action tags attempts to be fairly flexible and allow for the following:

```python

# This will be ignored since there is no action.
# FIXME: This is a bare fixme comment.
# TODO: This is a bare todo comment.

# This will be ignored since there is no action.
# FIXME(SRS): This comment includes my initials and is a popular way to signify that a
# person found an issue (and isn't directly responsible for fixing it).

# This will be tested since there is a valid action.
# FIXME(SRS): DATE: AFTER: 2022-01-01: This comment includes initials as well as a composite
# action and condition and will be tested.

# This will be ignored since no action handler exists (yet) for this.
# CRITICAL: SCHRÖDINGER: CAT: DEAD: Do not commit while cat is dead.

```

### Date Conditional Action Tags

Examples:

```python
# FIXME: DATE: AFTER: 2021-12-05: This will result in code `AH000: Date conditional action tag found (FIXME)
```

### Package Conditional Action Tags

Package conditional action tags attempt to locate and verify that a locally installed package is contained within a standard python packaging specifier.  This provides a utility to tag an area of code that may need to be refactored when a package is released (and locally available) that may contain a feature needed to bring in new functionality or prompt the need to refactor or remove a bugfix fixed upstream.

Examples:

```python
# FIXME: PACKAGE: VERSION: aws-lambda-powertools>=0.19.0: New feature should remove following bandaid code.
```

```python
# TODO: PACKAGE: VERSION: bungee-jump>=1.29: Can now jump with blindfold.  Add in new feature for blindfold jump.
```

```python
# CRITICAL: PACKAGE: VERSION: orm-uber-tool>=2.12.0,<=2.12.5: Bug introduced in module will cause CPU to smoke. Danger.
```

Utilizing this tag requires that following dependencies:

- [`packaging`](https://github.com/pypa/packaging): Developed by PyPa team and used in order to test a version against a specifier.
- [`importlib_metadata`](https://github.com/python/importlib_metadata): Developed by Python team and used in order to find the most relevant installed package version within your python environment.

## Error Codes

In the error code table the `{T}`/`{...}` represents a code and type related to the comment tag.  While 10 might be a short list it is most likely considered too long in most standards.  This project has opted to add in a few extras that don't directly overlap with other **fixme** related checkers as a way to offer some extended workflow and alerting functionality.

<!-- TODO(SRS): AFTER: DATE: 2022-01-01: New years resolution: Add in descriptions of types and related history. -->

| Code `{T}` | Type `{...}` | Description |
|:----------:|:-------------|:------------|
| `0` | `FIXME` | ... |
| `1` | `TODO` | ... |
| `2` | `XXX` | ... |
| `3` | `BUG` | ... |
| `4` | `REFACTOR` | ... |
| `5` | `REMOVEME` | ... |
| `6` | `LEGACY` | ... |
| `7` | `CRITICAL` | ... |
| `8` | `WARNING` | ... |

| Error codes | Description | Utility |
|:-----------:|:------------|:--------|
| `AH00{T}` | Date after condition met (`{...}`) | Good for tracking feature dates. |
| `AH01{T}` | Date before condition met (`{...}`) | Perhaps not very useful. |
| `AH40{T}` | Package version specifier condition met (`{...}`) | Refactoring against upstream changes. |
