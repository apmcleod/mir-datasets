import pytest

import os

import render_datasets


def test_render_one_flat_meta():
    key = 'abcd'
    rec = dict(url='http://ismir.net', metadata='beats',
               audio='yes', contents='40 bajillion songs')
    md = render_datasets.render_one(key, rec)
    assert len(md) > len(''.join(rec.values()))
    for v in rec.values():
        assert v in md


def test_render_one_list_meta():
    key = 'abcd'
    rec = dict(url='http://ismir.net', metadata=['beats', 'bars', 'sections'],
               audio='yes', contents='40 bajillion songs')
    md = render_datasets.render_one(key, rec)
    assert len(md) > len(''.join(rec.values()))
    for v in rec.values():
        assert v in md


def test_render_md(mir_datasets):
    for fmt in ('md', 'js'):
        res = render_datasets.render(mir_datasets, fmt)
        assert len(res) > len(''.join(str(mir_datasets.values())))


def test_main_call(mir_datasets_file, tmpdir, root_dir):
    script = os.path.join(root_dir, 'render_datasets.py')
    for fmt in ('md', 'js'):
        output_file = os.path.join(str(tmpdir), 'test_output.{}'.format(fmt))
        os.system('{} {} {}'.format(script, mir_datasets_file, output_file))