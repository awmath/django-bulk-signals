# CHANGELOG



## v0.4.2 (2024-01-23)

### Fix

* fix: pypi release ([`037c2ba`](https://github.com/awmath/django-bulk-signals/commit/037c2ba35c2e4531f61c09875e76b79de189fa34))


## v0.4.1 (2024-01-22)

### Chore

* chore: update pre-commit hooks ([`0a892e7`](https://github.com/awmath/django-bulk-signals/commit/0a892e7d3c4a4a009f96b3a7615e74283ff31ca1))

### Fix

* fix: non semantic commit has not triggered release ([`f6f076f`](https://github.com/awmath/django-bulk-signals/commit/f6f076f0a7edfbf0706ecca982dceea705565e36))

### Test

* test: added failing test for bulk method argument naming

See https://github.com/awmath/django-bulk-signals/pull/5 ([`da7e07b`](https://github.com/awmath/django-bulk-signals/commit/da7e07b068aeb009fbbfa8fd6b38f358f39d5a1c))

### Unknown

* Rename monkeypatch methods objects parameter to objs to match Django ([`0d1659b`](https://github.com/awmath/django-bulk-signals/commit/0d1659be4df2abdc5b5d49907ffef585fc837ec7))


## v0.4.0 (2023-04-29)

### Feature

* feat: signals can be skipped by a keyword argument ([`894e0ec`](https://github.com/awmath/django-bulk-signals/commit/894e0ec69e4f73290085b0e9c0141a0bef19cf3d))

### Unknown

* Merge pull request #4 from awmath/skip-signals

feat: signals can be skipped by a keyword argument ([`746ed2a`](https://github.com/awmath/django-bulk-signals/commit/746ed2a82b0e85cb9df42d6f6c28c2f05b5e6d0a))


## v0.3.0 (2023-04-28)

### Chore

* chore: maintenance ([`d6a5042`](https://github.com/awmath/django-bulk-signals/commit/d6a5042d991c680d770aeee4cdef57060dd470d4))

### Feature

* feat: post query update signal now passed the update count ([`e2424c9`](https://github.com/awmath/django-bulk-signals/commit/e2424c9a6033aab0164e94ff32c6699658291555))

### Unknown

* Merge pull request #3 from awmath/update-return-count

Update return count ([`8ac458f`](https://github.com/awmath/django-bulk-signals/commit/8ac458f8e4fcbda7d68838743aa2d8bf1d3b61a5))


## v0.2.1 (2022-12-07)

### Chore

* chore: cleanup README ([`983ef3e`](https://github.com/awmath/django-bulk-signals/commit/983ef3ee9cc0b0d5789c313e3d84013075e0d80d))

* chore: add pre-commit integration ([`3ed454e`](https://github.com/awmath/django-bulk-signals/commit/3ed454eee6b76d7a754d9d589855dd92496004ec))

### Fix

* fix: added missing tests module ([`9d4581c`](https://github.com/awmath/django-bulk-signals/commit/9d4581cbd0bc5a6f6d212e1ca796a1349dad2f79))

* fix: bulk_update no longer triggers the pre_update signal ([`809c86a`](https://github.com/awmath/django-bulk-signals/commit/809c86adcbe92d485ca0c1c48b59792ec26efdd4))


## v0.2.0 (2022-12-07)

### Chore

* chore: added codespaces support ([`37eaf6f`](https://github.com/awmath/django-bulk-signals/commit/37eaf6fd69a982b66b18102372696d65e540b712))

* chore: add version badges to README [skip ci] ([`b365715`](https://github.com/awmath/django-bulk-signals/commit/b365715c586b22f47d884883f73122d1a3bd855b))

### Ci

* ci: updated ci matrix tests to ressemble latest versions ([`192c5b5`](https://github.com/awmath/django-bulk-signals/commit/192c5b5fcb78aebf3c7884f8cafecf6b5b410156))

### Feature

* feat: added pre_*** action signals

The no_action kwargs for the bulk actions have been removed, as they
weren&#39;t part of the django default api. Also added all nulk action
args and kwargs to the signals as well. ([`ba6eb9a`](https://github.com/awmath/django-bulk-signals/commit/ba6eb9a869dd683d8675d6e45b41d67159ba0f13))


## v0.1.1 (2021-12-09)

### Chore

* chore: setup deployment on version tag ([`e6e1a99`](https://github.com/awmath/django-bulk-signals/commit/e6e1a996543d6126f9d511cc918fc52e88540c8b))

### Documentation

* docs: added app install to README.md ([`8b1ac60`](https://github.com/awmath/django-bulk-signals/commit/8b1ac6003549f4f9c67d7055ec45cf9823b4ab4e))

### Fix

* fix(ci): wrong branch for semantic release ([`b9758b1`](https://github.com/awmath/django-bulk-signals/commit/b9758b13f5410d13fb844d7524dcaa0231b6be94))

* fix(ci): coverage exports xml for codecov ([`7841dd7`](https://github.com/awmath/django-bulk-signals/commit/7841dd7dc9ff3dedbf477c8da43e8fe2c00667fb))

### Test

* test: restructured testing ([`6da7863`](https://github.com/awmath/django-bulk-signals/commit/6da7863f0f73b1e2715908986259d60f97eaa4a9))

* test: added codecov token and badge ([`92b5118`](https://github.com/awmath/django-bulk-signals/commit/92b5118ef79694331dcd5fd2e23bcb1435f39f55))

* test: fix django test versions ([`0bd7fd6`](https://github.com/awmath/django-bulk-signals/commit/0bd7fd635a23ce03293bf084849afaebfba30e13))

* test: switch django versions ([`9c9f665`](https://github.com/awmath/django-bulk-signals/commit/9c9f66527b370041cd6ef758805b38abe6830598))

### Unknown

* feature(ci): add semantic release versioning ([`f7e36cd`](https://github.com/awmath/django-bulk-signals/commit/f7e36cd46ebedbdca762b257162239b8c5ecc816))

* feature: added workflow badge ([`4525493`](https://github.com/awmath/django-bulk-signals/commit/4525493908704a69819ac5d3d697ff6c4f7059fa))

* feature:add pre-commit ([`59e32c2`](https://github.com/awmath/django-bulk-signals/commit/59e32c261d97917b945e71e4291c7164184f4110))

* feature: codefactor badge ([`29a3169`](https://github.com/awmath/django-bulk-signals/commit/29a3169512418dc1935fe95059cbfc7afb94e6fb))

* feature: initial complete setup ([`7fba3f5`](https://github.com/awmath/django-bulk-signals/commit/7fba3f50328709e1e725136797363b930ba17400))

* Initial commit ([`447ee90`](https://github.com/awmath/django-bulk-signals/commit/447ee9097f9b3405ee77e64885a38a92ab6e6fba))
