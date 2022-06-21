#!/usr/bin/env ruby
# Accepts one argument and pass it to a regular expression matching method

puts ARGV[0].scan(/hbttt?t?t?n/).join
