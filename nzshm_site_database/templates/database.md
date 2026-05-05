---
hide:
    - navigation
---
You are viewing the current version of the Database {{ version }}.

[Download the database](https://github.com/gns-science/nzshm-site-database/tree/{{ version }}/nzshm_site_database/data/sitedb.csv)

{% raw %}
{{ read_csv('../data/sitedb.csv') }}
{% endraw %}