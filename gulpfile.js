"use strict";

const gulp = require("gulp");
const uglify = require("gulp-uglify");
const concat = require("gulp-concat");
const minifyCss = require("gulp-minify-css");

gulp.task("minify-js", () => {
  return gulp
    .src([
      "./node_modules/jquery/dist/jquery.js",
      "./node_modules/jquery-validation/dist/jquery.validate.js",
      "./app/static/js/form-validation.js"
    ])
    .pipe(concat("index.min.js"))
    .pipe(uglify())
    .pipe(gulp.dest("./app/static/js/"));
});

gulp.task("minify-css", () => {
  return gulp
    .src("./app/static/css/site.css")
    .pipe(concat("site.min.css"))
    .pipe(minifyCss({ compatibility: "ie8" }))
    .pipe(gulp.dest("./app/static/css/"));
});

gulp.task("copy-fonts-to-static", () => {
  gulp
    .src(["./node_modules/font-awesome/fonts/*"])
    .pipe(gulp.dest("./app/static/vendor/fonts/font-awesome"));
});

gulp.task("minify", ["minify-js", "minify-css", "copy-fonts-to-static"]);
