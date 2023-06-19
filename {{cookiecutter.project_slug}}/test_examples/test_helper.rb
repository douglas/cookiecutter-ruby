# frozen_string_literal: true

require "minitest/autorun"
require "minitest/reporters"
require "mocha/minitest"

Minitest::Reporters.use! unless ENV["RM_INFO"]
