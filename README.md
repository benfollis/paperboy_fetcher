# paperboy_fetcher
Python binary that takes a list of RSS feed urls, and fetches the contents in a structure
that can be used by later portions of the paperboy pipeline.

Specifically given a provider named `FOO` and rss feed name `baz` will
download each article in the feed and store in the output directory files under the path `./FOO/baz/xxxx.json`
where `xxxx` is the md5 hash of the article contents.
