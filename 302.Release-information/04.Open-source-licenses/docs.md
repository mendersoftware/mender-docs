---
title: Open Source Licenses
taxonomy:
    category: docs
shortcode-core:
    active: false
process:
    twig: true
highlight:
    enabled: false
---

!!! This page and the subsections under Open Source Licenses list the open-source software components and applicable open-source licenses used
!!! in the default builds of Mender and specific Mender products, editions and tools. Together, they form the overall Open Source Licenses for Mender.

All open source licenses used in Mender with the default build are shown below.

Where copyright holder is missing, please refer to the repository of the software to identify the copyright holder(s).

<!-- Renders the content of every subpage here. -->
{% for child in page.children %}
<h2>{{ child.title }}</h2>
{{ child.content|raw }}
{% endfor %}
