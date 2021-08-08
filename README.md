# flake8-action-hero
A plugin for flake8 that performs conditional FIXME/TODO checks.

## Action Tags

### Date Conditional Action Tags

Examples:

```python
# FIXME: AFTER: DATE: 2021-12-05` will result in code `AH000: Date conditional action tag found (FIXME)
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

| Error codes | Description |
|:----------:|:------------|
| `AH00{T}` | Date conditional action tag found (`{...}`) |
| `AH40{T}` | Package conditional action tag found (`{...}`) |

