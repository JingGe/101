# Migrate Java submodules to a new repo

There are many different ways to migrate files/directories from one git repo to another, like creating log patch, format-patch, using filter-branch --subdirectory-filter. but it is difficult to create patch and modify the module structure simultaneously, e.g. migrate submodules of a submodule to the new repo and move them one level up to the root folder.

I figured out the simplest way to do it with [filter-repo ](https://github.com/newren/git-filter-repo)and then rebase.

As the example, we will migrate the elasticsearch connectors to the external repo

### **Filter the origin repo**

```
> git clone https://github.com/apache/flink.git
> cd flink // ~/patch/flink
> git filter-repo 
--path flink-connectors/flink-sql-connector-elasticsearch6 
--path flink-connectors/flink-sql-connector-elasticsearch7 
--path flink-connectors/flink-connector-elasticsearch6 
--path flink-connectors/flink-connector-elasticsearch7 
--path flink-connectors/flink-connector-elasticsearch-base
```

### Rebase the new repo

```
> git clone <external-connector-repo>
> git checkout -t origin/FLINK-26884-copy-elasticsearch-connectors
> git remote add flink-repo ~/patch/flink
> git fetch flink-repo
> git pull --rebase flink-repo master
```

Now, you should have all elasticsearch connectors in the new repo with all commit history. It is then up to you if you want to modify the module structure via refactoring.

### Rebase for the PR

Given the master branch is where your repo forked from. Before starting a PR, you should rebase your branch to the master branch.

```
> git pull --rebase origin master
> git push origin FLINK-26884-copy-elasticsearch-connectors -f
```

Now, you are ready to start the PR.
