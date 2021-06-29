const gulp = require("gulp");
const concat = require("gulp-concat");
const cleanCSS = require("gulp-clean-css");

function minifyCss() {
  return gulp
    .src("./app/static/css/site.css")
    .pipe(concat("site.min.css"))
    .pipe(cleanCSS({ compatibility: "ie8" }))
    .pipe(gulp.dest("./app/static/css/"));
}

function copyFontsToStatic() {
  return gulp
    .src(["./node_modules/font-awesome/fonts/*"])
    .pipe(gulp.dest("./app/static/vendor/fonts/font-awesome"));
}

const minify = gulp.series(minifyCss, copyFontsToStatic);

module.exports = {
  minify,
};
