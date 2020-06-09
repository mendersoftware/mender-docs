var vfile = require('to-vfile')
var report = require('vfile-reporter')
var unified = require('unified')
var parse = require('remark-parse')
var stringify = require('remark-stringify')
var remark2retext = require('remark-retext')
var english = require('retext-english')
var equality = require('retext-equality')

// Spelling
var retext = require('retext')
var spell = require('retext-spell')
var dictionary = require('dictionary-en')

// Readability
var readability = require('retext-readability')

// Passive voice
var passive = require('retext-passive')

// a vs an
var indefiniteArticle = require('retext-indefinite-article')

var path = require('path');
var walk = require('walk');
var pathToFiles = '..';
var options = {
    followLinks: false
};
var walker = walk.walk(pathToFiles, options);
walker.on('file', (root, fileStats, next) => {
    if (!fileStats.name.endsWith('docs.md')) {
        return next();
    }
    return unified()
        .use(parse)
        .use(
            remark2retext,
            unified()
                .use(english)
                .use(equality)
                .use(passive)
                .use(indefiniteArticle)
                .use(spell, dictionary)
                .use(readability, {age: 18})
        )
        .use(stringify)
        .process(vfile.readSync(path.join(root, fileStats.name)), function(err, file) {
            console.error(report(err || file))
            next();
        });
});
