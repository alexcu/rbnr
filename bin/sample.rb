#!/usr/bin/env ruby
require 'fileutils'

src_dir = ARGV[0]
raise 'Missing directory argument' if src_dir.nil?
dst_dir = ARGV[1]
num_times = ARGV[2].to_i
min_candidates = ARGV[3].to_i
photos = Dir["#{src_dir}/*.jpg"]

puts "#{src_dir} -> #{dst_dir} at sample #{num_times}"
sample_space = []
num_times.times.each do |idx|
  src_file = photos.sample
  next if sample_space.include?(src_file)
  basename = File.basename(src_file, '.jpg')
  candidates = basename.split('#').last.split(' ')
  next unless candidates.length >= min_candidates
  dst_file = "#{dst_dir}/Image#{idx + 1}\##{candidates.join(' ')}.jpg"
  puts "Copy #{src_file} -> #{dst_file}"
  FileUtils.cp(src_file, dst_file)
  sample_space << src_file
end
