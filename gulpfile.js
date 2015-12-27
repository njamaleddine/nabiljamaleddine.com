'use strict';

var gulp = require('gulp');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var minifyCss = require('gulp-minify-css');
var path = require('path');

gulp.task('minify-js', function() {
    return gulp.src([
        './node_modules/jquery/dist/jquery.js',
        './node_modules/jquery-validation/dist/jquery.validate.js',
        './app/static/js/form-validation.js'
        ])
        .pipe(concat('index.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('./app/static/js/'));
});

gulp.task('minify-css', function() {
  return gulp.src('./app/static/css/site.css')
    .pipe(concat('site.min.css'))
    .pipe(minifyCss({compatibility: 'ie8'}))
    .pipe(gulp.dest('./app/static/css/'));
});

gulp.task('minify', ['minify-js', 'minify-css']);