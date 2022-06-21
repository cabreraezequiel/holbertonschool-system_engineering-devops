#!/usr/bin/env ruby
# Accepts one argument and pass it to a regular expression matching method

#puts /School/.match(ARGV[0])
puts ARGV[0].scan(/School/).join
