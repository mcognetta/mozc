# Copyright 2010, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

{
  'variables': {
    'relative_dir': 'unix/ibus',
    'variables': {
      # SYSROOT directory path used for Chromium OS build
      'sysroot%': '',
    },
    'sysroot%': '<(sysroot)',
    'ibus_dependencies': [
      '../../base/base.gyp:base',
      '../../base/base.gyp:config_file_stream',
      '../../composer/composer.gyp:composer',
      '../../converter/converter.gyp:converter',
      '../../dictionary/dictionary.gyp:dictionary',
      '../../net/net.gyp:net',
      '../../prediction/prediction.gyp:prediction',
      '../../rewriter/rewriter.gyp:rewriter',
      '../../session/session.gyp:genproto_session',
      '../../session/session.gyp:session',
      '../../storage/storage.gyp:storage',
      '../../transliteration/transliteration.gyp:transliteration',
      '../../usage_stats/usage_stats.gyp:usage_stats',
    ],
    'ibus_include_dirs': [
      '<(sysroot)/usr/include/dbus-1.0',
      '<(sysroot)/usr/include/glib-2.0',
      '<(sysroot)/usr/include/ibus-1.0',
      '<(sysroot)/usr/lib/dbus-1.0/include',
      '<(sysroot)/usr/lib/glib-2.0/include'
    ],
    'ibus_libraries': [
      '-lcurl',
      '-ldbus-1',
      '-lglib-2.0',
      '-lgobject-2.0',
      '-libus',
    ],
    'ibus_ldflags': [
      '-L<(sysroot)/usr/lib',
    ],
  },
  'targets': [
    {
      'target_name': 'ibus_mozc_lib',
      'type': 'static_library',
      'sources': [
        'engine_registrar.cc',
        'key_translator.cc',
        'mozc_engine.cc',
        'path_util.cc',
        'session.cc',
      ],
      'include_dirs': [
        '<@(ibus_include_dirs)',
      ],
    },
    {
      'target_name': 'ibus_mozc',
      'type': 'executable',
      'sources': [
        'main.cc',
      ],
      'dependencies': [
        '<@(ibus_dependencies)',
        'ibus_mozc_lib',
      ],
      'include_dirs': [
        '<@(ibus_include_dirs)',
      ],
      'libraries': [
        '<@(ibus_libraries)',
      ],
      'ldflags': [
        '<@(ibus_ldflags)',
      ]
    },
    {
      'target_name': 'ibus_mozc_test',
      'type': 'executable',
      'sources': [
        'key_translator_test.cc',
        'path_util_test.cc',
        'session_test.cc',
      ],
      'dependencies': [
        '<@(ibus_dependencies)',
        '../../testing/testing.gyp:gtest_main',
        'ibus_mozc_lib',
      ],
      'include_dirs': [
        '<@(ibus_include_dirs)',
      ],
      'libraries': [
        '<@(ibus_libraries)',
      ],
      'ldflags': [
        '<@(ibus_ldflags)',
      ]
    },
  ],
}