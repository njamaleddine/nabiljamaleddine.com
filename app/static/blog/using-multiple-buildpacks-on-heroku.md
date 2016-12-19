<!-- # Using Multiple Buildpacks on Heroku -->
<!-- Published 2015-12-23 -->

While setting up an application to use [Postgis](http://postgis.net/) on [Heroku](https://www.heroku.com/) I realized that Postgis wasn't installed by default.

Using custom libraries is possible through the declaration of custom buildpacks. David Dollar created the awesome [heroku-buildpack-multi](https://github.com/ddollar/heroku-buildpack-multi) repository for the purpose of including multiple buildpacks in the build process.

It's as simple as creating a `.buildpacks` file with each line specifying the git url for the buildpack you're going to use.

**Ex:**

<pre>
https://github.com/cyberdelia/heroku-geo-buildpack.git#1.3
https://github.com/heroku/heroku-buildpack-python.git
</pre>


To enable multiple buildpacks enter the following heroku cli command into the terminal; it's necessary in specifying which buildpack your app will use:

```
heroku buildpacks:set https://github.com/ddollar/heroku-buildpack-multi.git
```


### Very important note:

Setting the Heroku `BUILDPACK_URL` is **NOT** the same as entering the above command (at least not at this time). Heroku will not set the proper buildpack unless you enter the above command.

To ensure that your app is using the proper buildpack, take a look at the settings page of your heroku app, the buildpack specified should read "Multipack".

