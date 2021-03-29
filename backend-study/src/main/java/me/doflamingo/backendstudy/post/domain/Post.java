package me.doflamingo.backendstudy.post.domain;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.validation.constraints.Size;
import java.time.LocalDateTime;

@Entity @AllArgsConstructor
@Getter @Builder @NoArgsConstructor
public class Post {

  @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Size(min = 1, max = 50, message = "제목은 1자에서 50자 사이입니다.")
  private String title;

  private String content;

  @Size(min = 1, max = 30, message = "작성자 Id는 1자에서 30자 사이입니다.")
  private String writerId;

  private LocalDateTime createdAt;

  private LocalDateTime updatedAt;
}
