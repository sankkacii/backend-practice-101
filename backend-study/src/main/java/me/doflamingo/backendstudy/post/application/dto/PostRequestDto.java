package me.doflamingo.backendstudy.post.application.dto;

import lombok.Builder;
import lombok.Getter;

import javax.validation.constraints.Size;

@Getter @Builder
public class PostRequestDto {

  @Size(min = 1, max = 50, message = "제목은 1자에서 50자 사이입니다.")
  private String title;

  private String content;

  @Size(min = 1, max = 50, message = "작성자 Id는 1자에서 30자 사이입니다.")
  private String writerId;
}
