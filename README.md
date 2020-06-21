<p align="center">
  <img alt="Django Template" title="Django Template" src="./assets/logo.png" width="128">
</p>

<h1 align="center">Django Template</h1>

<p align="center">
  <a href="#overview">Overview</a> |
  <a href="#features">Features</a>
</p>

## Overview

Django Template was designed to start Django project quickly

## Features

- [django-split-settings](https://github.com/sobolevn/django-split-settings) for clear setting separation
- [django-environ](https://github.com/joke2k/django-environ) for managing secret values
- Run test with pytest
- default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review

## Update Related Project

```shell
# 1. github-template Repository
git remote add template https://github.com/AsheKR/github-template.git
```

## Bots

### TODO Bot

See [its page](https://probot.github.io/apps/todo/) for further configuration. This template sets two variables: autoAssign and exclude, which sets the user resposible for the push to be the assignee of the issue, and ignores the .gitattributes file from issue opening. We suggest keeping this way.

### Welcome Bot

This bot are actually three bots into one. See the central [page](https://probot.github.io/apps/welcome/) for further configuration. There are three variables, each being the message posted by the bot: newIssueWelcomeComment, newPRWelcomeComment, and firstPRMergeComment. You may customize these messages if you wish.
