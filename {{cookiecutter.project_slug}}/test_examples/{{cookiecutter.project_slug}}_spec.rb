{% set class_name = cookiecutter.project_name.title().replace(' ', '') -%}
# frozen_string_literal: true

require "rspec/autorun"

require_relative "../{{cookiecutter.project_slug}}"

describe {{ class_name }} do
  it "prints message when run" do
    expect { {{ class_name }}.run }
      .to(output(a_string_including("Let's go!")).to_stdout)
  end
end
