#!/usr/bin/env ruby
# Accepts one argument and pass it to a regular expression matching method

puts ARGV[0].scan(/hb?tn/).join
