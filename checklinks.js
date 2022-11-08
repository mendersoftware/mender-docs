#! /usr/bin/env node

import { remark } from 'remark';
import { engine } from 'unified-engine';

import yargs from 'yargs';

var argv = yargs().scriptName('checklinks').usage('$0 [paths]...').help().argv;

engine(
  {
    // Standard engine configuration
    processor: remark,
    files: argv._.length > 0 ? argv._ : ['.'],
    extensions: ['md'],
    pluginPrefix: 'remark',
    packageField: 'remarkConfig',
    quiet: !argv.verbose,
    color: argv.color,
    frail: true
  },
  (error, failed) => {
    if (error || failed === 1) throw error;
  }
);
