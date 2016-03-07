/*
 * Author: Michael J. Ruschak
 * Description:
 * Ruschak Invoice and Expense gulp configuration file
 */

var gulp = require('gulp');
var shell = require('gulp-shell');

gulp.task('bootstrap-copy', function() {
    // SASS Files
    gulp.src('bower_components/bootstrap/dist/css/*.min.css').pipe(gulp.dest('common/static/bootstrap/css'));
    gulp.src('bower_components/bootstrap/dist/css/*.map').pipe(gulp.dest('common/static/bootstrap/css'));

    // JS Files
    gulp.src('bower_components/bootstrap/dist/js/bootstrap.min.js').pipe(gulp.dest('common/static/bootstrap/js'));

    // FONT Files
    gulp.src('bower_components/bootstrap/dist/fonts/*').pipe(gulp.dest('common/static/bootstrap/fonts'));
});

gulp.task('run', function() {
    gulp.src('.').pipe(shell('python3 manage.py runserver 172.16.30.129:8000'));
});

gulp.task('default', ['bootstrap-copy']);
