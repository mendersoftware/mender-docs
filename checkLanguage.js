#! env /usr/bin/node

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

if (process.argv.length != 3) {
    console.error("Usage checkLanguage <file>")
    return
}

var file = vfile.readSync({path: process.argv[2]})

unified()
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
    .process(file, function(err, file) {
        console.error(report(err || file))
    });
