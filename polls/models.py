from django.db import models


class Question(models.Model):
	# 文字のフィールド
	question_text = models.CharField(max_length=200)
	# 日時フィールド
	pub_date = models.DateTimeField('date published')
	# オブジェクトの表現
	def __str__(self):
		return self.question_text
	# タイムゾーン関連
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	# リレーションシップ
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	# デフォルト値を0に設定
	votes = models.IntegerField(default=0)
	# オブジェクトの表現
	def __str__(self):
		return self.question_text