{% set class_name = cookiecutter.project_name.title().replace(' ', '') -%}
# frozen_string_literal: true

require "test_helper"

require_relative "../{{cookiecutter.project_slug}}"

class {{ class_name }}Test < Minitest::Test
  def test_prints_a_message_when_run
    assert_output(/Let's go!/) { {{ class_name }}.run }
  end
end
