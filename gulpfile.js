'use strict';

var gulp = require('gulp');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');

var DESTINATION = './static/js/';

gulp.task('minify', function() {
    return gulp.src([
        './node_modules/jquery/dist/jquery.js',
        './node_modules/jquery-validation/dist/jquery.validate.js',
        './static/js/form-validation.js'
        ])
        .pipe(concat('index.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest(DESTINATION));
});
