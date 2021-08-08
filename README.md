# flake8-action-hero
A plugin for flake8 that performs conditional FIXME/TODO checks.

Example: `FIXME: AFTER: DATE: 2021-12-05` will result in code `AH000: Date conditional action tag found (FIXME)`

## Action Tags

### Date Conditional Action Tags

### Package Conditional Action Tags

Package conditional action tags attempt to locate and verify that a locally installed package is contained within a standard python packaging specifier.  This provides a utility to tag an area of code that may need to be refactored when a package is released (and locally available) that may contain a feature needed to bring in new functinoality or prompt the need to refactor or remove a bugfix fixed upstream.

Utilizing this tag requires that following dependencies:

- [`packaging`](https://github.com/pypa/packaging): Developed by PyPa team and used in order to test a version against a specifier.
- [`importlib_metadata`](https://github.com/python/importlib_metadata): Developed by Python team and used in order to find the most relevant installed package version within your python environment.

## Error Codes

In the error code table the `{T}`/`{...}` represents a code and type related to the comment tag.

| Code `{T}` | Type `{...}` |
|:---------:|:-----|
| `0` | `FIXME` |
| `1` | `TODO` |
| `2` | `XXX` |
| `3` | `BUG` |
| `4` | `REFACTOR` |
| `5` | `REMOVEME` |
| `6` | `LEGACY` |

| Error codes | Description |
|:----------:|:------------|
| `AH00{T}` | Date conditional action tag found (`{...}`) |
| `AH40{T}` | Package conditional action tag found (`{...}`) |

