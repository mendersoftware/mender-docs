var remark = require('remark');
var parse = require('remark-parse');
var stringify = require('remark-stringify');
var engine = require('unified-engine');

engine(
  {
    // Standard engine configuration
    processor: remark,
    files: ['.'],
    extensions: ['md'],
    pluginPrefix: 'remark',
    packageField: 'remarkConfig',
    injectedPlugins: [parse, stringify],
    color: true,
    frail: true
  },
  (error, failed) => {
    if (error || failed === 1) throw error;
  }
);
