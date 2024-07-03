const gulp = require('gulp')
const glob = require('glob')
const svgstore = require('gulp-svgstore')
const svgmin = require('gulp-svgmin')
const merge = require('merge-stream')

gulp.task('svg-sprites', async function () {
    return merge(glob.sync('./project/templates_tw/static/sprites/*').map(function(spritesDir) {
        return gulp.src(spritesDir + '/*.+(svg)')
            .pipe(svgmin())
            .pipe(svgstore({'inlineSvg': true}))
            .pipe(gulp.dest('./project/templates_tw/static/dist/sprites/'))
    }))
})
